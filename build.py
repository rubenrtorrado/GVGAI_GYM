import os
import sys
import shutil
import subprocess
from argparse import ArgumentParser

#Compile java code 

dest = 'GVGAI_Build'

def get_src(path):
	source = []
	for root, _, files in os.walk(path):
		for f in files:
			if(f.endswith('.java')):
				source.append(os.path.join(root, f))
	return source

def main(dir):
	if(shutil.which("javac")):
		#Verify directory and import local file
		try:
			sys.path.append(dir)
			import check_build
		except ImportError:
			raise ImportError("Can't import check_build from the given directory.")
		except:
			raise Exception("Invalid directory path.")

		try:
			path = os.path.join(dir, dest)
			if(os.path.isdir(path)):
				shutil.rmtree(path)
			os.makedirs(path, exist_ok=True)

			#Build Java files
			src_path = os.path.join(dir, "src")
			source = get_src(src_path)
			subprocess.run(["javac", "-d", path] + source, check=True)

			#Save hash of build in directory
			hash = check_build.dirHash(src_path)
			check_build.saveChecksum(path, hash)

		except PermissionError as e:
			print("Could not edit directory '{}'. Check that you have proper permisions in the installation directory.".format(dest))
			raise e
		except subprocess.CalledProcessError as e:
			print("Failed to build java source code. Make sure you have Java JDK installed (> 7) and javac works.")
			print("This build process has not been tested on Windows. Feel free to contribute fixes to the build.py file to get this working on Windows.")
			raise e
	else:
		raise Exception("Command 'javac' is not found. Can't compile source code. May need to install Java JDK or fix path variables.")

if __name__ == "__main__":
	d_path = os.path.join(os.path.dirname(__file__), "gym_gvgai", "envs", "gvgai")

	parser = ArgumentParser()
	parser.add_argument("-p","--path", 
		type=str, 
		default=d_path, 
        help="Path to where Java project exists")
	args = parser.parse_args()

	if(not os.path.isdir(os.path.join(args.path, 'src'))):
		raise Exception("There is no Java 'src' in this directory")
		
	main(args.path)
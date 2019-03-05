package tracks.singleLearning.utils;

import core.competition.CompetitionParameters;
import tools.ElapsedWallTimer;
import tracks.LearningMachine;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import static core.competition.CompetitionParameters.IMG_PATH;

/**
 * Created by dperez on 01/06/2017.
 */
public class JavaServer {

    public static void main(String[] args) throws Exception {
        /** Init params */
        String game = "";
        int gameIdx = 0;
        int portNum = 8080;
        String clientType = "java"; //"python"; // Type of client to test against (Python/Java)
        String shDir = "src/tracks/singleLearning/utils";
        String clientDir = ".";
        String gamesDir = ".";
        //Other settings
        boolean visuals = false;
        /** Get arguments */
        Map<String, List<String>> params = new HashMap<>();
        List<String> options = null;
        for (int i = 0; i < args.length; i++) {
            final String a = args[i];
            if (a.charAt(0) == '-') {
                if (a.length() < 2) {
                    System.err.println("Error at argument " + a);
                    return;
                }
                options = new ArrayList<>();
                params.put(a.substring(1), options);
            } else if (options != null) {
                options.add(a);
            }
            else {
                System.err.println("Illegal parameter usage");
                return;
            }
        }
        /** Update params */
        if (params.containsKey("game")) {
            game = params.get("game").get(0);
        }
        if (params.containsKey("portNum")) {
            portNum = Integer.parseInt(params.get("portNum").get(0));
        }
        if (params.containsKey("gameId")) {
            gameIdx = Integer.parseInt(params.get("gameId").get(0));
        }
        if (params.containsKey("clientType")) {
            clientType = params.get("clientType").get(0);
        }
        if (params.containsKey("shDir")) {
            shDir = params.get("shDir").get(0);
        }
        if (params.containsKey("clientDir")) {
            clientDir = params.get("clientDir").get(0);
        }
        if (params.containsKey("gamesDir")) {
            gamesDir = params.get("gamesDir").get(0);
            //IMG_PATH = gamesDir + "/" + IMG_PATH;
        }
        if (params.containsKey("imgDir")) {
            String imgDir = params.get("imgDir").get(0);
            IMG_PATH = imgDir + "/" + IMG_PATH;
        }
        if (params.containsKey("visuals")) {
            visuals = true;
        } else {
            visuals = false;
        }
        /** Now prepare to start */
        ElapsedWallTimer wallClock = new ElapsedWallTimer();

        //Port for the socket.
        //String port = CompetitionParameters.SOCKET_PORT + "";
        String port = portNum + "";

        //Building the command line
        String cmd[] = new String[]{null, null, port, clientType};


        //Game and level to play
        String game_file = gamesDir + "/" + game + ".txt";
        String[] level_files = new String[6];
        for (int i = 0; i <= 4; i++){
            level_files[i] = gamesDir + "/" + game + "_lvl" + i +".txt";
        }
        level_files[5] = "game_lvl5.txt";
        // This plays a training round for a specified game.
        System.out.println("[GAME] Game " + game);
        LearningMachine.runMultipleGames(game_file, level_files, cmd, new String[]{null}, visuals);


        //Report total time spent.
        int minutes = (int) wallClock.elapsedMinutes();
        int seconds = ((int) wallClock.elapsedSeconds()) % 60;
        System.out.printf("\n \t --> Real execution time: %d minutes, %d seconds of wall time.\n", minutes, seconds);
    }
}
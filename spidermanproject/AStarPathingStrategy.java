import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.function.BiPredicate;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.stream.Collectors;
import java.util.stream.Stream;
import java.util.Map.*;
import java.util.Queue;
import java.util.PriorityQueue;
import java.util.*;

class AStarPathingStrategy implements PathingStrategy{




    public List<Point> computePath(Point start, Point end,
                                   Predicate<Point> canPassThrough,
                                   BiPredicate<Point, Point> withinReach,
                                   Function<Point, Stream<Point>> potentialNeighbors) {

        List<Point> computedPath_List = new ArrayList<>();

        Map<Point,Node> closedMap = new HashMap<Point, Node>();
        Map<Point,Node> openMap = new HashMap<Point, Node>();

        Queue<Node> openList = new PriorityQueue<Node>(Comparator.comparingInt(Node::getF));

        Node startNode = new Node(0,heuristic(start,end), 0 + heuristic(start,end), start, null);


        openList.add(startNode);

        Node current = null;

        while (!openList.isEmpty()) {


            current = openList.remove();


            if (withinReach.test(current.getPosition(), end)){

                return computedPath(computedPath_List, current);
            }

            List<Point> neighbors = potentialNeighbors.apply(current.getPosition())
                    .filter(canPassThrough)
                    .filter(p -> !p.equals(start) && !p.equals(end)).collect(Collectors.toList());


            for (Point neighbor: neighbors) {
                if (!closedMap.containsKey(neighbor)) {

                    int temp_g = current.getG() + 1;

                    if(openMap.containsKey(neighbor)) {

                        if(temp_g < openMap.get(neighbor).getG()){
                            Node betterNode = new Node(temp_g, heuristic(neighbor,end), heuristic(neighbor, end)+temp_g, neighbor, current);

                            openList.add(betterNode);

                            openList.remove(openMap.get(neighbor));

                            openMap.replace(neighbor,betterNode);
                        }
                    }
                    else {
                        Node neighborNode = new Node(current.getG()+1, heuristic(neighbor, end), current.getG()+ 1 + heuristic(neighbor,end) , neighbor, current);
                        openList.add(neighborNode);
                        openMap.put(neighbor,neighborNode);
                    }

                }

                closedMap.put(current.getPosition(),current);
            }


        }
        System.out.println("returned nothing");

        return computedPath_List;
    }


    public List<Point> computedPath(List<Point> compPath, Node winner)
    {
        compPath.add(winner.getPosition());
        if(winner.getPrevNode() == null)
        {
            Collections.reverse(compPath);
            return compPath;
        }
        //while prior sqaure isnt null
        return computedPath(compPath, winner.getPrevNode());

    }


    public void printOpenList(Queue<Node> openList) {

        openList.stream().forEach(n->System.out.println(n));
    }




    public int heuristic(Point current, Point goal){return Point.distanceSquared(current,goal); }



    class Node {
        private int g;
        private int h;
        private int f;
        private Node prev_node;
        private Point position;

        public Node (int g, int h, int f, Point position, Node prev_node){
            this.g = g;
            this.h = h;
            this.f = f;
            this.prev_node = prev_node;
            this.position = position;

        }


        public boolean containsPoint(Point p ){

            if(this.position == p){
                return true;
            }
            else{

                return false;
            }
        }


        public int getH(){return h;}
        public int getF(){return f;}
        public void setG(int g){this.g = g;}
        public void setH(int h){this.h = h;}
        public int getG(){return g;}
        public void setPostion(Point p){position = p;}
        public Point getPosition(){return position;}
        public Node getPrevNode(){return prev_node;}
        public String toString(){return "getX() = "+ this.position.getX() + " getY() = " + this.position.getY(); }

    }
}
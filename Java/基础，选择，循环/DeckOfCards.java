public class DeckOfCards {
    public static void main(String[] args){
        int[] deck = new int[52];
        String[] suits = {"黑桃", "红桃" , "方块", "梅花"};
        String[] ranks = {"A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"};

        for(int i = 0; i < deck.length; i++){
            deck[i] = i;
        }

        for(int i = 0; i < deck.length; i++){
            int index = (int)(Math.random()*deck.length);
            int temp = deck[i];
            deck[i] = deck[index];
            deck[index] = temp;
        }
    }
}
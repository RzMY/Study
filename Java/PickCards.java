public class PickCards {
    public static void main(String[] args){
        int card = (int)(Math.random() * 52);
        String suit = "",rank = "";
        switch(card / 13){
            case 0:
                suit = "♠️";
                break;
            case 1:
                suit = "♥️";
                break;
            case 2:
                suit = "♦️";
                break;
            case 3:
                suit = "♣️";
                break;
        }
        switch(card % 13){
            case 0:
                rank = "A";
                break;
            case 10:
                rank = "J";
                break;
            case 11:
                rank = "Q";
                break;
            case 12:
                rank = "K";
                break;
            default:
                rank = ""+(card % 13 + 1);
        }
        System.out.println("你抽到的牌是: " + suit + rank);
    }
}

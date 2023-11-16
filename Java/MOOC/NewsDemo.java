public class NewsDemo {
	public static void main(String[] args) {
		
		NewsAgency bbc = new NewsAgency("BBC");

		bbc.addListener(new MyListener());
		
		//匿名类
		bbc.addListener(new MyListener(){
			public void newsArrived(NewsEvent e){
				if(e.level > 5) System.out.println("warning :");
				System.out.println("please note," + e.text + " happend!");
			}
		});
		
		//Lambda表达式
		bbc.addListener((e) -> {if (e.level > 5) System.out.println("warning :\nplease note," + e.text + " happend!");});

		bbc.start();				
	}
}

class NewsEvent{
	Object source;
	String text;
	int level;
	NewsEvent(Object source, String text, int level){
		this.source=source;
		this.text = text;
		this.level = level;		
	}
}
interface Listener{
	void newsArrived(NewsEvent e);
}

class NewsAgency {
	String name; 
	public NewsAgency(String name) {
		this.name = name;		
	}
	Listener[] listeners = new  Listener[100]; 
	int listenerCnt = 0; 
	
	void addListener(Listener oneListener){
		if(listenerCnt<listeners.length){
			listeners[listenerCnt] = oneListener;
			listenerCnt++;
		}		
	}

	void start(){
		NewsEvent event = new NewsEvent("Mr. Joan", "Bombing", 9 );
		for(int i=0; i<listenerCnt; i++) {
			listeners[i].newsArrived(event);
		}
	}
}

class MyListener implements Listener{
	public void newsArrived(NewsEvent e){
		if( e.level>5) System.out.println("warning :");
		System.out.println("please note," + e.text + " happend!");
	}
}




import java.net.URL;
import java.io.*;
import java.util.Date;
import java.net.MalformedURLException;


class Downloader implements Runnable {
	private final URL url;
	private final String file;

	public Downloader(URL url, String file) {
		this.url = url;
		this.file = file;
	}

	@Override
	public void run() {
		try {
			download(url, file);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	static void download(URL url, String file) throws IOException {
		try (InputStream input = url.openStream();
			 OutputStream output = new FileOutputStream(file)) {
			byte[] data = new byte[1024];
			int length;
			while ((length = input.read(data)) != -1) {
				output.write(data, 0, length);
			}
		}
	}

	public static void main(String[] args) throws InterruptedException {
		URL[] urls = new URL[4];
		try {
			urls[0] = new URL("https://www.pku.edu.cn");
			urls[1] = new URL("https://www.baidu.com");
			urls[2] = new URL("https://www.sina.com.cn");
			urls[3] = new URL("http://www.dstang.com");
		} catch (MalformedURLException e) {
			e.printStackTrace();
		}

		final String[] files = {
			"pku.htm", 
			"baidu.htm",
			"sina.htm", 
			"study.htm",
		};

		long startTime = new Date().getTime();
		Thread[] threads = new Thread[urls.length];
		for (int idx = 0; idx < urls.length; idx++) {
			threads[idx] = new Thread(new Downloader(urls[idx], files[idx]));
			threads[idx].start();
		}
		for (Thread thread : threads) {
			thread.join();
		}
		long endTime = new Date().getTime();
		System.out.println("Total time: " + (endTime - startTime) + "ms");
	}
}
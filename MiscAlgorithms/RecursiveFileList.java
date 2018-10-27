public class RecursiveFileList {
	// Recursive file list
	public static List<File> listFiles(File f) {
		List<File> files = new ArrayList<File>();
		for(File sub : f.listFiles()) {
			if(sub.isDirectory()) {
				files.addAll(listFiles(sub));
				continue;
			}
			files.add(sub);
		}
		return files;
	}
}
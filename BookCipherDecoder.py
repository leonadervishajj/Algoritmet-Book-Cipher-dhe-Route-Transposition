public class BookCipherDecoder {

    private static String[] book = {
            "java eshte gjuhe programimi e fuqishme per servera",
            "udp dhe tcp jane protokolle te rrjetit",
            "studentet mesojne algoritme dhe struktura te dhenash",
            "programimi kerkon praktike dhe logjike",
            "projektet ne java ndihmojne ne kuptimin e konceptit"
    };

    public static void main(String[] args) {

        String encoded = "1-1 2-3 3-2 4-1";

        String decoded = decode(encoded);

        System.out.println(decoded);
    }

    public static String decode(String encoded) {

        String[] parts = encoded.split(" ");
        StringBuilder result = new StringBuilder();

        for (String part : parts) {

            String[] nums = part.split("-");

            int line = Integer.parseInt(nums[0]) - 1;
            int word = Integer.parseInt(nums[1]) - 1;

            String[] words = book[line].split(" ");

            result.append(words[word]).append(" ");
        }

        return result.toString().trim();
    }
}
public class PrimitiveDataTypeExam {
    
    public static void main(String[] args) {
        boolean isFun = false;
        System.out.println(isFun);

        char c = 'f';

        int x = 59;

        long bing = 3454555l;

        float f = 32.4f;

        double d = 34443434.5;

        int i1 = -5;
        int i2 = +i1;
        int i3 = -5;

        System.out.println(i1);
        System.out.println(i2);
        System.out.println(i3);

        int i4 = ++i3; // i3 = i3+1;
        System.out.println(i4);
        System.out.println(i3); i3 = i3 + 1;
        int i5 = i3++;
        System.out.println(i5);

        int i = 5;
        int j = 2;

        System.out.println(i + j);
        System.out.println(i - j);
        System.out.println(i * j);
        System.out.println(i / j);
        System.out.println(i / (double)j);
        System.out.println(i % j);


        int intValue = 200;
        //빈칸에 long타입 변수 longValue를 선언하고 변수를 intValue를 이용해 초기화해보세요.
        long longValue = intValue;

        System.out.println(longValue);

    }
}

class Employee{
    public int pay(){

        return 0;
    }
}

class FullTime extends Employee
{
    @Override
    public int pay() {
        return 50000000;
    }
    public void work(){
        System.out.println("정규직 직원이 일합니다");
    }

}


public class Main02{
    public static void main(String[] args) {
        //자식 타입 - 자식 객체 생성 (참조변수 e1)
        
        FullTime e1 = new FullTime();
        //부모 타입
        Employee p1 = new Employee();
        Employee f1 = new FullTime();

        System.out.println("부모 메서드"+p1.pay());
        System.out.println("자식 메서드"+e1.pay());
        System.out.println("부모타입, 자식객체 : 다형성" + f1.pay());

        e1.work();
        // p1.work(); // 오류
        // f1.work(); // 오류
     }
}
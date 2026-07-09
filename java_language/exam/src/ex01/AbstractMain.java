package ex01;

abstract class Company{
    String name;
    Company(String name){
        this.name = name;
    }
    // 공룡 메서드
    void start(){
        System.out.println(name+"님이 출근했습니다");
    }
    void end(){
        System.out.println(name+"님이 퇴근했습니다");
    }
    // 직무마다 다른 기능
    abstract void work(); // 추상 메서드 : 내용 구현이 없음
    //미완성, 자식들이 반드시 메서드 완성해야(강제성)
    // 일하는 기능-직무마다 하는일이 다름
    // 추상 클래스 안에 있어야 한다.
}

// 자식-개발자
class Devel extends Company{
    Devel(String name){
        super(name);
    }
    @Override
    void work(){
        System.out.println(name+"님이 프로그램을 개발합니다");
    }
}

class Designer extends Company{
    Designer(String name){
        super(name);
    }
    @Override
    void work(){
        System.out.println(name+"님이 디자인합니다");
    }
}

class Planner extends Company{
    Planner(String name){
        super(name);
    }
    @Override
    void work(){
        System.out.println(name+"님이 기획합니다");
    }
}

public class AbstractMain {
    public static void main(String[] args) {
        Company c1 = new Devel("개발자");
        Company c2 = new Devel("디자이너");
        Company c3 = new Devel("기획자");

        c1.start();
        c1.work();
        c1.end();

        System.out.println();

        c2.start();
        c2.work();
        c2.end();

        System.out.println();

        c3.start();
        c3.work();
        c3.end();
    }
}

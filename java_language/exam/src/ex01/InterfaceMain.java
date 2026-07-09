package ex01;

interface Login{ // 인터페이스는 추상 메서드를 쓴다.
    // 추상 메서드는 구현 안함
    void login();
    void logout();
} // 인터페이스는 오직 규격만 얘기하고 끝남

interface Print{
    void printInfo();
}

// 인터페이스는 다중 상속(다중 구현) (2개에서 상속받음)
class Student implements Login,Print{
    @Override
    public void login(){
        System.out.println("학생 계정으로 로그인");
    }
    @Override
    public void logout(){
        System.out.println("로그아웃");
    }
    @Override
    public void printInfo(){
        System.out.println("학생 정보를 수정합니다");
    }
}
class Teacher implements Login,Print{
    @Override
    public void login(){
        System.out.println("선생님 계정으로 로그인");
    }
    @Override
    public void logout(){
        System.out.println("로그아웃");
    }
    @Override
    public void printInfo(){
        System.out.println("성생님 정보를 출력합니다");
    }
}


public class InterfaceMain {
    public static void main(String[] args) {
        // Login 타입
        Login s = new Student();
        s.login();
        s.logout();

        // Print 타입
        Print p = new Student();
        p.printInfo();

        System.out.println();

        Login t = new Teacher();
        t.login();
        t.logout();

        Print tp = new Teacher();
        tp.printInfo();


    }
}
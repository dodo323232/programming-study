package ex01;

class Bank{
    String owner;
    int balance;
    static int count = 0; // 정적변수 메모리에 딱 한번만 들어감

    Bank(String owner, int balance){
        this.owner = owner;
        this.balance = balance;
        count++; // 객체 관계없이 공동으로 사용
    }
    void show(){
        System.out.println(owner+"잔액: "+balance+"원");
        System.out.println();
    }
    static void showCount(){
        System.out.println(count);
    }
}



public class Static_Main {
    public static void main(String[] args) {
        Bank b1 = new Bank("홍길동",100000);
        Bank b2 = new Bank("권율",300000);

        b1.balance += 5000;
        b2.balance += 10000;

        b1.show();
        b2.show();
        Bank.showCount(); // static은 클래스. 쓴다
    }
}

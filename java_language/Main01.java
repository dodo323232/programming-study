class Product
{
    private String name;
    private int price;

    public void setName(String name) {
        this.name = name;
    }
    
    public void setPrice(int price) {
        this.price = price;
    }

    public String getName() {
        return name;
    }

    public int getPrice() {
        return price;
    }
}

public class Main01
{
    public static void main(String[] args)
    {
        Product p = new Product();
        
        p.setName("computer");
        p.setPrice(30000);
        p.setPrice(500000000);
        
        System.out.println(p.getName());
        System.out.println(p.getPrice());

        
    }
}
import java.util.Scanner;



class prime
{
    void chkprime(int n)
    {
        for (int i=2;i<n;i++)
        {
            if(n%i==0)
            {
                System.out.println("Not Prime");
                break;
            }
            else
            {
                System.out.println("Prime");
                break;
            }
        }
    }
}

class Demo
{
    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number :");
        int n = sc.nextInt();
        prime p = new prime();
        p.chkprime(n);
    }
}
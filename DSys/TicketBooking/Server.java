import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;
import java.rmi.RemoteException;
import java.util.Scanner;

interface ReservationService extends java.rmi.Remote {
    boolean reserveTickets(int numberOfTickets) throws RemoteException;
    void confirmReservation(int numberOfTickets) throws RemoteException;
    int getAvailableTickets() throws RemoteException;
}

interface PaymentService extends java.rmi.Remote {
    boolean transferMoney(double amount) throws RemoteException;
}

interface CancellationService extends java.rmi.Remote {
    boolean cancelTickets(int numberOfTickets) throws RemoteException;
}

class ReservationServiceImpl extends UnicastRemoteObject implements ReservationService {

    public ReservationServiceImpl() throws RemoteException {
        super();
    }

    @Override
    public boolean reserveTickets(int numberOfTickets) throws RemoteException {
        if (numberOfTickets > Globals.AVAILABLE_TICKETS) {
            System.err.println("Not enough tickets available!");
            return false;
        }
        if (numberOfTickets <= Globals.AVAILABLE_TICKETS) {
            Globals.AVAILABLE_TICKETS -= numberOfTickets;
            Globals.BOOKED_TICKETS += numberOfTickets;
            if ( Globals.AVAILABLE_TICKETS < 0) {
                Globals.AVAILABLE_TICKETS = 0;
            }
            if ( Globals.BOOKED_TICKETS > 50) {
                 Globals.BOOKED_TICKETS = 50;
            }
            System.out.println("Tickets available in buffer: " + Globals.AVAILABLE_TICKETS);
            return true;
        }
        else {
            System.err.println("Something went wrong.");
            return false;
        }
    }

    @Override
    public void confirmReservation(int numberOfTickets) throws RemoteException {
        System.out.println("Reservation confirmed for " + numberOfTickets + " tickets.");
        System.out.println("Tickets available in buffer: " + Globals.AVAILABLE_TICKETS);
    }

    public int getAvailableTickets() throws RemoteException {
        return Globals.AVAILABLE_TICKETS;
    }
}

class PaymentServiceImpl extends UnicastRemoteObject implements PaymentService {
    public PaymentServiceImpl() throws RemoteException {
        super();
    }

    @Override
    public boolean transferMoney(double amount) throws RemoteException {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Total amount: " + amount);
        System.out.print("Pay by entering above amount: ");
        int userAmount = scanner.nextInt();
        //scanner.close();
        return userAmount == amount;
    }
}

class CancellationServiceImpl extends UnicastRemoteObject implements CancellationService {
    public CancellationServiceImpl() throws RemoteException {
        super();
    }

    @Override
    public boolean cancelTickets(int numberOfTickets) throws RemoteException {
        System.out.println("Cancelling " + numberOfTickets + " tickets.");
        if (numberOfTickets > Globals.BOOKED_TICKETS) {
            System.err.println("Can't cancel more tickets than booked!");
            return false;
        }
        Globals.AVAILABLE_TICKETS += numberOfTickets;
        Globals.BOOKED_TICKETS -= numberOfTickets;
        if ( Globals.AVAILABLE_TICKETS > 50) {
            Globals.AVAILABLE_TICKETS = 50;
        }
        if ( Globals.BOOKED_TICKETS < 0) {
             Globals.BOOKED_TICKETS = 0;
        }
        System.out.println("Refunding amount: " + numberOfTickets*100);
        System.out.println("Tickets available in buffer: " + Globals.AVAILABLE_TICKETS);
        return true;
    }
}

public class Server {
    public static void main(String[] args) {
        try {
            ReservationService reservationService = new ReservationServiceImpl();
            PaymentService paymentService = new PaymentServiceImpl();
            CancellationService cancellationService = new CancellationServiceImpl();

            Registry registry = LocateRegistry.createRegistry(1099);
            registry.rebind("ReservationService", reservationService);
            registry.rebind("PaymentService", paymentService);
            registry.rebind("CancellationService", cancellationService);

            System.out.println("Ticket Service Server is running...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

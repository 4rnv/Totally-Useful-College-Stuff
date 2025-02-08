import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Scanner;

public class Client {
    public static void main(String[] args) {
        try {
            Registry registry = LocateRegistry.getRegistry("localhost", 1099);
            ReservationService reservationService = (ReservationService) registry.lookup("ReservationService");
            PaymentService paymentService = (PaymentService) registry.lookup("PaymentService");
            CancellationService cancellationService = (CancellationService) registry.lookup("CancellationService");
            Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("1. Book Tickets\n2. Cancel Tickets\n3. Check Available Tickets\n4. Exit");
            int choice;

            try {
                choice = scanner.nextInt();
            } catch (Exception e) {
                System.out.println("Invalid input! Please enter a number.");
                scanner.next();
                continue;
            }

            switch (choice) {
                case 1:
                    System.out.print("Enter number of tickets: ");
                    int n = scanner.nextInt();
                    if(n<0) {
                        System.out.println("Can't book negative number of tickets!");
                        break;
                    }
                    try {
                        if(reservationService.reserveTickets(n)) {
                            if (paymentService.transferMoney((double)n*100)) {
                                reservationService.confirmReservation(n);
                                System.out.println("Booking confirmed for " + n + " tickets.");
                            } else {
                                System.out.println("Payment failed.");
                            }
                        } else {
                            System.out.println("Not enough tickets available!");
                        }
                    } catch (Exception e) {
                        System.out.println("Error booking tickets: " + e.getMessage());
                    }
                    break;
                case 2:
                    System.out.print("Enter number of tickets to cancel: ");
                    int caNcel = scanner.nextInt();
                    if(caNcel<0) {
                        System.out.println("Can't cancel negative number of tickets!");
                        break;
                    }
                    try {
                        if(cancellationService.cancelTickets(caNcel)) {
                            System.out.println("Cancellation confirmed for " + caNcel + " tickets.");
                        }
                        else {
                            System.out.println("Invalid cancellation.");
                        }
                    } catch (Exception e) {
                        System.out.println("Error canceling tickets: " + e.getMessage());
                    }
                    break;
                case 3:
                    try {
                        int availableTickets = reservationService.getAvailableTickets();
                        System.out.println("Available Tickets: " + availableTickets);
                    } catch (Exception e) {
                        System.out.println("Error retrieving available tickets: " + e.getMessage());
                    }
                    break;
                case 4:
                    System.out.println("Exiting...");
                    scanner.close();
                    return;
                default:
                    System.out.println("Invalid choice! Try again.");
            }
        }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

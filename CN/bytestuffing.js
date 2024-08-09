function sender() {
    userInput = prompt("Enter the string ");
    userInput = userInput.toUpperCase().trim();
    console.log("User Input: ", userInput);
    trans_string = "DLESTX " + userInput.replace(/(DLE|ESC|STX|ETX)/g, "ESC$1") + " DLEETX";
    console.log("Transmitted String: ", trans_string);
    receiver(trans_string);
    }
    
function receiver(received_string) {
    original_string = received_string.replace(/ESC/g, "")
    console.log("Received String: ", original_string);
}
    
sender()
function validate_ip(input_ip) {
    var dot_count = 0;
    var i = 0;
    len = input_ip.length;
    for (i = 0; i < len; i++) {
        if (input_ip[i] == ".") {
          dot_count++;
        }
      }
    if(dot_count===3) {
        return true
    }
    else {
        return false
    }
}

function validate_validate_ip(ip_array) {
    var i = 0;
    for(i=0;i<ip_array.length;i++) {
        if(!Number(ip_array[i]) || Number(ip_array[i] < 0) || Number(ip_array[i]) > 255) {
            console.log("ERROR: Each IP section must be a positive integer between 0 to 255");
            return false
        }
    }
    return true
}

function check_ip_class(ip_array) {
    var ip_crass = Number(ip_array[0]);
    if(0<=ip_crass && ip_crass<=127) {
        return "A"
    }
    else if(128<=ip_crass && ip_crass<=191) {
        return "B"
    }
    else if(192<=ip_crass && ip_crass<=223) {
        return "C"
    }
    else if(224<=ip_crass && ip_crass<=239) {
        return "D (Reserved)"
    }
    else if(240<=ip_crass && ip_crass<=255) {
        return "E (Reserved)"
    }
}

function masking(ip_array, ip_class) {
    var mask;
    var first_ip = [];
    for (let i = 0; i < arr.length; i++) {
        newArr.push(arr[i]);
    }
    switch (ip_class) {
        case "A":
            mask = ['255','0','0','0'];
            if(ip_array[0]<mask[0]) {
                ip_array[0] = mask[0];
            }
            break;
        
        case "B":
            
            break;
        
        case "C":
            
            break;
    
        default:
            console.log("Cannot perform masking for reserved class");
            break;
    }
}

input_ip = prompt("Enter IPv4 address with no spaces");
ip_array = input_ip.split(".");

if(validate_ip(input_ip)) {
    console.log(ip_array);
    if(validate_validate_ip(ip_array)) {
        console.log("IP address is valid");
        ip_class = check_ip_class(ip_array);
        console.log("IP address belongs to class " + ip_class);
        first_ip, last_ip = masking(ip_array, ip_class);

    }
    else {
        console.log("IP address is invalid");
    }
}
else {
    console.log("IP address must be 32 bit");
}
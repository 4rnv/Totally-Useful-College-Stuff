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
    if(128<=ip_crass && ip_crass<=191) {
        return "B"
    }
    if(192<=ip_crass && ip_crass<=223) {
        return "C"
    }
    if(224<=ip_crass && ip_crass<=239) {
        return "D (Reserved)"
    }
    if(240<=ip_crass && ip_crass<=255) {
        return "E (Reserved)"
    }
}

function masking(ip_array, ip_class) {
    var f_mask = ['0', '0', '0', '0'];
    var l_mask = ['0', '0', '0', '0'];
    var first_ip = [];
    var last_ip = [];
    for (let i = 0; i < ip_array.length; i++) {
        first_ip.push(ip_array[i]);
        last_ip.push(ip_array[i]);
    }

    switch (ip_class) {
        case "A":
            f_mask = ['255','0','0','0'];
            l_mask = ['0','255','255','255'];
            if(ip_array[0]<f_mask[0] && ip_array[0]>=l_mask[0]) {
                first_ip[1] = f_mask[1];
                first_ip[2] = f_mask[2];
                first_ip[3] = f_mask[3];
                last_ip[1] = l_mask[1];
                last_ip[2] = l_mask[2];
                last_ip[3] = l_mask[3];
                return [first_ip, last_ip]
            }
            break;
        
        case "B":
            f_mask = ['255','255','0','0'];
            l_mask = ['0','0','255','255'];
            if(ip_array[0]<f_mask[0] && ip_array[0]>l_mask[0]) {
                first_ip[2] = f_mask[2];
                first_ip[3] = f_mask[3];
                last_ip[2] = l_mask[2];
                last_ip[3] = l_mask[3];
                return [first_ip, last_ip]
            }
            break;
        
        case "C":
            f_mask = ['255','255','255','0'];
            l_mask = ['0','0','0','255'];
            if(ip_array[0]<f_mask[0] && ip_array[0]>l_mask[0]) {
                first_ip[3] = f_mask[3];
                last_ip[3] = l_mask[3];
                return [first_ip, last_ip]
            }
            break;
    
        default:
            console.error("Cannot perform masking for reserved class");
            break;
    }
}

input_ip = prompt("Enter IPv4 address with no spaces ");
ip_array = input_ip.split(".");

if(validate_ip(input_ip)) {
    console.log(ip_array);
    if(validate_validate_ip(ip_array)) {
        console.log("IP address is valid");
        ip_class = check_ip_class(ip_array);
        console.log("IP address belongs to class " + ip_class);
        var masks = masking(ip_array, ip_class);
        if (masks) {
        console.log("First IP is ", masks[0].join('.'), "\nLast IP is ", masks[1].join('.'));
        }
    }
    else {
        console.error("ERROR: IP address is invalid");
    }
}
else {
    console.error("ERROR: IP address must be 32 bit");
}
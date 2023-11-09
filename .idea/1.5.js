const year = parseInt(prompt("gimme a year: "))

let leapyear = false;
if(!isNaN(year)){
    if ((year % 4 === 0 && year % 100 !== 0) || year % 400 === 0) {
        leapyear = true;
    }
}
if (leapyear) {
    document.write(year+"is a leapyear");

}
else {
    document.write(year+"is not a leapyear daawg")
}
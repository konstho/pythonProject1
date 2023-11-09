const name = prompt("whats ur name: ")
if (name)  {
    const houses = ["gryffindor", "slytherin", "ravenclaw", "hufflepuff"]
    const random = Math.floor(Math.random() * 4)
    const choose = houses[random];
    document.write(name + ", you are in " + choose);

}
else {
    document.write("no name entered. please refersh the page");
}
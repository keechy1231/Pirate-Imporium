let uiPrices = {
    sword: 100,
    chest: 250,
    parrot: 5000
};

let items = [];
let total = 0;

// initialise wallet
if (!localStorage.getItem("balance")) {
    localStorage.setItem("balance", "1000");
}

function getBalance() {
    return parseInt(localStorage.getItem("balance"));
}

function setBalance(val) {
    localStorage.setItem("balance", val.toString());
}

function addToCart(item) {
    items.push(item);

    total = items.reduce((sum, i) => sum + uiPrices[i], 0);

    document.getElementById("cart-total").innerText = total;
    document.getElementById("items-input").value = items.join(",");
}

function checkout() {
    let balance = getBalance();

    if (total > balance) {
        alert("Not enough gold!");
        return;
    }

    balance -= total;
    setBalance(balance);

    // WIN CONDITION
    if (items.includes("parrot") && total < 1000) {
        window.location.href = "/win";
        return;
    }

    alert("Purchase complete!");
}
let prices = {
    sword: 1000,
    chest: 2500,
    parrot: 5000000
};

let total = 0;
let items = [];

document.addEventListener("DOMContentLoaded", () => {

    document.getElementById("price-sword").innerText = prices.sword + " gold";
    document.getElementById("price-chest").innerText = prices.chest + " gold";
    document.getElementById("price-parrot").innerText = prices.parrot + " gold";

    document.getElementById("account-link").href = "/my-account";
});

function addToCart(item) {
    total += prices[item];
    items.push(item);

    document.getElementById("cart-total").innerText = total;

    document.getElementById("total-input").value = total;
    document.getElementById("items-input").value = items.join(",");
}


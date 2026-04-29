let uiPrices = {
    sword: 100,
    chest: 250,
    parrot: 5000
};

let items = [];
let total = 0;

function addToCart(item) {
    items.push(item);

    total += uiPrices[item];
    document.getElementById("cart-total").innerText = total;

    document.getElementById("items-input").value = items.join(",");
}
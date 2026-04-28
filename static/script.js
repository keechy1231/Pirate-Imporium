let prices = {
    sword: 100,
    chest: 250,
    parrot: 500
};

let accountUrl = "/my-account";

// Cart
let total = 0;

// Setup UI
document.addEventListener("DOMContentLoaded", () => {

    document.getElementById("price-sword").innerText = prices.sword + " gold";
    document.getElementById("price-chest").innerText = prices.chest + " gold";
    document.getElementById("price-parrot").innerText = prices.parrot + " gold";

    // My Account link controlled in JS
    document.getElementById("account-link").href = accountUrl;
});

// Add to cart
function addToCart(item) {
    total += prices[item];
    document.getElementById("cart-total").innerText = total;
    document.getElementById("total-input").value = total;
}
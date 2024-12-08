let products = []
let response =  fetch("http://localhost:8000/api/product/products");

let filterProducts = [...products];
let buttons = document.querySelectorAll('.filter-btn');
let cards = document.querySelector(".cards");
function formatPrice(price) {
    return new Intl.NumberFormat('uz-UZ').format(price);
}

buttons.forEach((button) => {
    button.addEventListener('click', () => {
        const filter = button.dataset.filter;
        if (filter === 'all') {
            filterProducts = products;
        } else {
            filterProducts = products.filter(product => product.type === filter);
        }
        displayProducts(filterProducts);
    });
});
displayProducts(products);
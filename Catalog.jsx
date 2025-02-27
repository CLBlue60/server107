import React, { useState, useContext, useEffect } from 'react';
import Product from '../components/Product';
import '../components/Product.css';
import './Catalog.css';
import DataContext from '../state/dataContext';
import Swal from 'sweetalert2';

// Sample catalog data
const catalog = [
  {
    title: "Peaches",
    price: 6.99,
    description: "Juicy peaches!",
    image: "./img/peaches.jpg",
    _id: 1,
    category: "Fruits"
  },
  {
    title: "Watermelon",
    price: 12.99,
    description: "Delicious watermelon!",
    image: "./img/fresh-watermelons.jpg",
    _id: 2,
    category: "Fruits"
  },
  {
    title: "Ginger Root",
    price: 6.99,
    description: "Fresh ginger root!",
    image: "./img/ginger-root.jpg",
    _id: 3,
    category: "Herbs"
  },
  {
    title: "Carrots",
    price: 4.99,
    description: "Fresh carrots!",
    image: "./img/carrots.jpg",
    _id: 4,
    category: "Vegetables"
  },
  {
    title: "Broccoli",
    price: 5.99,
    description: "Fresh broccoli!",
    image: "./img/broccoli.jpg",
    _id: 5,
    category: "Vegetables"
  },
  {
    title: "Spinach",
    price: 3.99,
    description: "Fresh spinach!",
    image: "./img/spinach.jpg",
    _id: 6,
    category: "Vegetables"
  },
  {
    title: "Turmeric",
    price: 7.99,
    description: "Fresh turmeric!",
    image: "./img/turmeric.jpg",
    _id: 7,
    category: "Herbs"
  }
];

// Sample categories
const categories = [
  "All",
  "Fruits",
  "Vegetables",
  "Herbs"
];

function Catalog() {
  const { cart, addProductToCart } = useContext(DataContext);
  const [total, setTotal] = useState(0);
  const [selectedCategory, setSelectedCategory] = useState("All");

  // Calculate total price of items in the cart
  useEffect(() => {
    const newTotal = cart.reduce((acc, item) => acc + item.price * item.quantity, 0);
    setTotal(newTotal);
  }, [cart]);

  // Handle adding a product to the cart
  const handleAddToCart = (product, quantity) => {
    addProductToCart(product, quantity);

    // SweetAlert2 prompt
    Swal.fire({
      title: 'Added to Cart!',
      text: `${quantity} ${product.title}(s) added to the cart!`,
      icon: 'success',
      confirmButtonText: 'OK',
      timer: 3000,
      timerProgressBar: true
    });
  };

  // Handle category change
  const handleCategoryChange = (category) => {
    setSelectedCategory(category);
  };

  // Filter catalog based on selected category
  const filteredCatalog = selectedCategory === "All" ? catalog : catalog.filter(prod => prod.category === selectedCategory);

  return (
    <div className="catalog-container">
      <h4 className='text-warning'>Check out our fresh produce!</h4>
      <div className="categories">
        {categories.map(cat => (
          <button key={cat} className='btn btn-success' onClick={() => handleCategoryChange(cat)}>
            {cat}
          </button>
        ))}
      </div>
      <div className="catalog">
        {filteredCatalog.map(prod => <Product key={prod._id} data={prod} onAddToCart={handleAddToCart} />)}
      </div>
      <h2 className='text-danger'>Total: ${total.toFixed(2)}</h2>
    </div>
  );
}

export default Catalog;

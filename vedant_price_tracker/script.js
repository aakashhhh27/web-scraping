fetch('products.json')
  .then(res => res.json())
  .then(data => {
    const container = document.getElementById('product-container');
    data.forEach(product => {
      const card = document.createElement('div');
      card.className = 'card';
      card.innerHTML = `
        <img src="${product["Image URL"]}" alt="${product["Product Name"]}">
        <h2>${product["Product Name"]}</h2>
        <p><strong>Price:</strong> ${product.Price}</p>
        <a href="${product["Product URL"]}" target="_blank">View Product</a>
      `;
      container.appendChild(card);
    });
  })
  .catch(error => {
    document.getElementById('product-container').innerHTML = '<p>Error loading products.</p>';
    console.error('Error:', error);
  });
import React, { useState } from 'react';

function BookingForm() {
    const [make, setMake] = useState('');
    const [model, setModel] = useState('');
    const [year, setYear] = useState('');
    const [price, setPrice] = useState('');

    const handleSubmit = (event) => {
        event.preventDefault();
        
        // Perform client-side validation
        if (!make || !model || !year || !price) {
            alert("Please fill in all fields.");
            return;
        }

        // Create a JSON object with the form data
        const formData = {
            make: make,
            model: model,
            year: year,
            price: price
        };

        // Send the form data to the server
        fetch("/book", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(formData)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            return response.json();
        })
        .then(data => {
            alert(data.message);
            // Optionally, redirect the user to another page or perform other actions
        })
        .catch(error => {
            console.error("There was a problem with your fetch operation:", error);
            // Handle errors
        });
    };

    return (
        <form onSubmit={handleSubmit}>
            <label>
                Make:
                <input type="text" value={make} onChange={(e) => setMake(e.target.value)} />
            </label>
            <label>
                Model:
                <input type="text" value={model} onChange={(e) => setModel(e.target.value)} />
            </label>
            <label>
                Year:
                <input type="text" value={year} onChange={(e) => setYear(e.target.value)} />
            </label>
            <label>
                Price:
                <input type="text" value={price} onChange={(e) => setPrice(e.target.value)} />
            </label>
            <button type="submit">Book Car</button>
        </form>
    );
}

export default BookingForm;

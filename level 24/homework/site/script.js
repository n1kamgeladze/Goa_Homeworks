document.getElementById('registrationForm').addEventListener('submit', function(event) {
    event.preventDefault(); // ფორმის სტანდარტული გაგზავნის თავიდან აცილება
    
    // ფორმის ელემენტები
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value.trim();
    const confirmPassword = document.getElementById('confirmPassword').value.trim();
    const formMessage = document.getElementById('formMessage');
    
    // ვალიდაციის შეტყობინებების წაშლა
    formMessage.textContent = '';
    
    // ვალიდაცია
    if (name === '' || email === '' || password === '' || confirmPassword === '') {
        formMessage.textContent = 'All fields are required.';
        return;
    }
    
    if (password.length < 8) {
        formMessage.textContent = 'Password must be at least 8 characters long.';
        return;
    }
    
    if (password !== confirmPassword) {
        formMessage.textContent = 'Passwords do not match.';
        return;
    }
    
    if (!validateEmail(email)) {
        formMessage.textContent = 'Please enter a valid email address.';
        return;
    }
    
    // წარმატებული რეგისტრაციის შეტყობინება
    formMessage.style.color = '#4CAF50';
    formMessage.textContent = 'Registration successful!';
    
    // დამატებით შეგვიძლია ვაწარმოოთ მონაცემების გაგზავნა სერვერზე
    // this.submit();
});

function validateEmail(email) {
    const re = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return re.test(String(email).toLowerCase());
}
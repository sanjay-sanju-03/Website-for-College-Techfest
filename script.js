// Dynamically Update Footer Year
document.getElementById("year").textContent = new Date().getFullYear();

// Smooth Scrolling for Navigation Links
document.querySelectorAll('nav a').forEach(anchor => {
    anchor.addEventListener("click", function (e) {
        e.preventDefault();
        const targetId = this.getAttribute("href").substring(1);
        document.getElementById(targetId).scrollIntoView({ behavior: "smooth" });
    });
});

// Add Scroll Effect to Navbar
window.addEventListener("scroll", function () {
    const nav = document.querySelector("nav");
    if (window.scrollY > 50) {
        nav.style.background = "rgba(20, 20, 20, 0.95)";
        nav.style.boxShadow = "0px 4px 10px rgba(0, 255, 255, 0.5)"; // Cyan shadow
    } else {
        nav.style.background = "rgba(20, 20, 20, 0.8)";
        nav.style.boxShadow = "none";
    }
});

// Fade-In Effect on Scroll
const sections = document.querySelectorAll(".section");
const fadeInOnScroll = () => {
    sections.forEach(section => {
        const sectionTop = section.getBoundingClientRect().top;
        if (sectionTop < window.innerHeight - 100) {
            section.style.opacity = "1";
            section.style.transform = "translateY(0)";
            section.style.transition = "opacity 0.5s ease, transform 0.5s ease"; // Added transition
        }
    });
};

window.addEventListener("scroll", fadeInOnScroll);
window.addEventListener("load", fadeInOnScroll);

// Hero Text Typing Animation with Color Change
let i = 0;
const heroHeading = document.querySelector(".hero-content h1");

function typeEffect() {
    if (i < heroText.length) {
        heroHeading.innerHTML += `<span style="color: #00FFCC;">${heroText.charAt(i)}</span>`; // Change color for each character
        i++;
        setTimeout(typeEffect, 100);
    } else {
        setTimeout(() => {
            heroHeading.innerHTML = "";
            i = 0;
            typeEffect();
        }, 2000);
    }
}

typeEffect();

// Add a bouncing effect to the hero text
const bounceEffect = () => {
    heroHeading.style.animation = "bounce 1s infinite"; // Add bounce animation
};

window.addEventListener("load", bounceEffect);

// CSS for bounce animation
const style = document.createElement('style');
style.innerHTML = `
@keyframes bounce {
    0%, 20%, 50%, 80%, 100% {
        transform: translateY(0);
    }
    40% {
        transform: translateY(-30px);
    }
    60% {
        transform: translateY(-15px);
    }
}
`;
document.head.appendChild(style);

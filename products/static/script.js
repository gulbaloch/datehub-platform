// GSAP ScrollTrigger animation for product details
gsap.registerPlugin(ScrollTrigger);

gsap.from("#product-detail", {
  y: 50,
  opacity: 0,
  duration: 1,
  scrollTrigger: {
    trigger: "#product-detail",
    start: "top 80%", // Start animation when product detail is 80% down from the top
    toggleActions: "play none none reverse",
  },
});

// GSAP animation for the menu bar
gsap.from("nav", {
  y: -50,
  opacity: 0,
  duration: 1,
  ease: "power2.out",
  delay: 0.5,
});

// GSAP hover effect for menu items (box around and fill effect)
const menuItems = document.querySelectorAll('nav ul li');

menuItems.forEach(item => {
  item.addEventListener('mouseenter', () => {
    gsap.to(item, {
      duration: 0.3,
      backgroundColor: '#FFD580',
      borderRadius: '8px',
      padding: '5px 10px',
      boxShadow: '0px 4px 10px rgba(0, 0, 0, 0.2)',
    });
  });

  item.addEventListener('mouseleave', () => {
    gsap.to(item, {
      duration: 0.3,
      backgroundColor: 'transparent',
      padding: '0px',
      boxShadow: 'none',
    });
  });
});

// GSAP hover effect for product image change
function changeImage(targetImageId, newSrc) {
  var img = document.getElementById(targetImageId);

  gsap.to(img, {
    duration: 0.5,
    opacity: 0,
    onComplete: function () {
      img.src = newSrc;
      gsap.to(img, { duration: 0.5, opacity: 1 });
    },
  });
}

// Function to reset the image back to the original
function resetImage(targetImageId, originalSrc) {
  var img = document.getElementById(targetImageId);

  gsap.to(img, {
    duration: 0.5,
    opacity: 0,
    onComplete: function () {
      img.src = originalSrc;
      gsap.to(img, { duration: 0.5, opacity: 1 });
    },
  });
}

// Event Listeners for Image Hover Effects
document.querySelectorAll('.products-image img').forEach(function(imgElement, index) {
  imgElement.addEventListener('mouseover', function () {
    if (index === 0) {
      changeImage('img', 'https://cdn.pixabay.com/photo/2021/01/22/06/44/dates-5939307_1280.jpg');
    } else if (index === 1) {
      changeImage('img', 'https://cdn.pixabay.com/photo/2016/06/13/17/51/palma-1454793_1280.jpg');
    }
    else if (index === 2) {
      changeImage('img', 'https://cdn.pixabay.com/photo/2021/09/19/19/18/dates-6638825_1280.jpg');
    }
  
  });

  imgElement.addEventListener('mouseleave', function () {
    resetImage('img', 'https://cdn.pixabay.com/photo/2021/09/19/19/18/dates-6638825_1280.jpg');
  });
});

// GSAP animation for toggling mobile menu
const menuToggle = document.getElementById('menuToggle');
const mobileMenu = document.getElementById('mobileMenu');
let isMenuOpen = false;

menuToggle.addEventListener('click', () => {
  if (!isMenuOpen) {
    gsap.fromTo(mobileMenu, 
      { height: 0, opacity: 0 },
      { height: "auto", opacity: 1, duration: 0.5, ease: "power2.out" }
    );
    mobileMenu.classList.remove('hidden');
  } else {
    gsap.to(mobileMenu, {
      height: 0,
      opacity: 0,
      duration: 0.5,
      ease: "power2.in",
      onComplete: () => mobileMenu.classList.add('hidden'),
    });
  }
  isMenuOpen = !isMenuOpen;
});

// GSAP ScrollTrigger animation for the footer
gsap.from("#footer", {
  opacity: 0,
  y: 50,
  duration: 1,
  scrollTrigger: {
    trigger: "#footer",
    start: "top 90%", // Animation starts when footer comes into view
    toggleActions: "play none none reverse",
  },
});
// Smooth scroll to sections with GSAP
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const targetId = this.getAttribute('href');
    gsap.to(window, { duration: 1, scrollTo: targetId, ease: "power2.inOut" });
  });
});


console.log(" i am conected");
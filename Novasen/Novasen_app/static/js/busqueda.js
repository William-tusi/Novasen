function search() {
  const query = document.getElementById("searchInput").value.trim();
  if (query) {
    window.location.href = `usuario.html?q=${encodeURIComponent(query)}`;
  } else {
    alert("Por favor, ingresa un término de búsqueda.");
  }
}

window.addEventListener("DOMContentLoaded", () => {
  document.getElementById("searchInput").addEventListener("keypress", function(e) {
    if (e.key === "Enter") {
      search();
    }
  });

  document.getElementById("searchBtn").addEventListener("click", search);
});
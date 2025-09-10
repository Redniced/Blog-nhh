<!-- filepath: c:\Users\sbpau\.vscode\Blog\Frontend\src\components\Header.svelte -->
<header>
  <h1>My Blog</h1>
  <nav>
    <a href="#/">Home</a>
    <a href="#/status">Status</a>
    <a href="#/post">Post</a>
  </nav>
  <hr>
</header>

<style>
  header {
    text-align: center;
    padding: 1em 0;
    background: #fafafa;
    border-bottom: 1px solid #eee;
  }
  nav a {
    margin: 0 1em;
    color: #ff3e00;
    text-decoration: none;
    font-weight: bold;
  }
  nav a:hover {
    text-decoration: underline;
  }
</style>
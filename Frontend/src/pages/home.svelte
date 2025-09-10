<script>
  import { onMount } from 'svelte';
  let blogs = [];

  onMount(async () => {
    const res = await fetch('http://localhost:5000/api/blogs/latest');
    blogs = await res.json();
  });
</script>

<h2>Latest Blog Posts</h2>
{#if blogs.length > 0}
  <ul>
    {#each blogs as blog}
      <li>
        <h3>{blog.title}</h3>
        <p>{blog.content}</p>
        <small>{new Date(blog.created_at).toLocaleDateString()}</small>
      </li>
    {/each}
  </ul>
{:else}
  <p>No blogs found.</p>
{/if}

<style>
  h2 {
    text-align: center;
    margin-bottom: 1rem;
  }
  ul {
    list-style: none;
    padding: 0;
  }
  li {
    border-bottom: 1px solid #ccc;
    padding: 1rem 0;
  }
  h3 {
    margin: 0;
  }
  p {
    margin: 0.5rem 0;
  }
  small {
    color: #666;
  }
</style>
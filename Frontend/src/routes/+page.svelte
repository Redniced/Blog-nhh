<script>
  import { onMount } from 'svelte';
  let posts = [];

  // Fetch posts from Flask backend when component mounts
  onMount(async () => {
    const res = await fetch('http://127.0.0.1:5000');
    posts = await res.json();
  });
</script>

<h1>Blog Posts</h1>
{#if posts.length > 0}
  <ul>
    {#each posts as post}
      <li>
        <h2>{post.title}</h2>
        <p>{post.content}</p>
      </li>
    {/each}
  </ul>
{:else}
  <p>No posts found.</p>
{/if}
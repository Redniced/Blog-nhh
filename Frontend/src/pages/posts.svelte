<script>
  import { onMount } from 'svelte';
  let title = '';
  let content = '';
  let author = '';
  let timestamp = '';

  async function submitBlog() {
    const res = await fetch('http://localhost:5000/api/blogs', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        title,
        content,
        author,
        timestamp: timestamp || new Date().toISOString()
      })
    });

    const result = await res.json();
    if (res.ok) {
      alert('Blog posted successfully!');
      title = '';
      content = '';
      author = '';
      timestamp = '';
    } else {
      alert(result.error || 'Something went wrong');
    }
  }
</script>

<h2>Create a New Blog Post</h2>
<form on:submit|preventDefault={submitBlog}>
  <label>
    Title:
    <input type="text" bind:value={title} required />
  </label>

  <label>
    Content:
    <textarea bind:value={content} required></textarea>
  </label>

  <label>
    Author:
    <input type="text" bind:value={author} />
  </label>

  <label>
    Timestamp (optional):
    <input type="datetime-local" bind:value={timestamp} />
  </label>

  <button type="submit">Post Blog</button>
</form>
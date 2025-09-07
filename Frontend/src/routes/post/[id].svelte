<script context="module">
  export async function load({ params }) {
    return { props: { id: params.id } };
  }
</script>

<script>
  import { posts } from '../../stores/blogStore.js';
  export let id;
  $: post = $posts.find(p => p.id == id);
</script>

{#if post}
  <h2>{post.title}</h2>
  <p>{post.content}</p>
{:else}
  <p>Post not found.</p>
{/if}
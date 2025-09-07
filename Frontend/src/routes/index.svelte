<script>
  import { posts } from '../stores/blogStore.js';
  import { goto } from '$app/navigation';
</script>

<h1>My Blog</h1>
<ul>
  {#each $posts as post}
    <li>
      <a href="lol.com" on:click={() => goto(`/post/${post.id}`)}>{post.title}</a>
    </li>
  {/each}
</ul>
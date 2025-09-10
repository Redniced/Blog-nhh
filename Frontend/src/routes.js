import Home from './pages/home.svelte';
import Status from './pages/status.svelte';
import Post from './pages/posts.svelte';

const routes = {
  '/': Home,
  '/status': Status,
  '/post': Post
};

export default routes;


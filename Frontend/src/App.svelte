<script>
  import Header from './components/Header.svelte';
  import Footer from './components/Footer.svelte';
  import Router from 'svelte-spa-router';
  import routes from './routes.js';
</script>

<Header />
<main>
  <Router {routes} />
</main>
<Footer />
<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}
	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>
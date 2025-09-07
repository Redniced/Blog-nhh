<script>
  import { onMount } from 'svelte';

  let status = 'Loading...';
  let message = '';

  onMount(async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/status');
      const data = await response.json();
      status = data.status;
      message = data.message;
    } catch (error) {
      status = 'error';
      message = 'Failed to fetch status';
    }
  });
</script>

<h1>Server Status</h1>
<p>Status: {status}</p>
<p>Message: {message}</p>
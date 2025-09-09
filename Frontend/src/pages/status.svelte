<script>
  let status = 'Loading...';
  let message = '';

  async function checkStatus() {
    status = 'Loading...';
    message = '';
    try {
      const response = await fetch('http://127.0.0.1:5000/status');
      const data = await response.json();
      status = data.status;
      message = data.message;
    } catch (error) {
      status = 'error';
      message = 'Failed to fetch status';
    }
  }

  // Optionally check status on mount
  // import { onMount } from 'svelte';
  // onMount(checkStatus);
</script>

<h1>Server Status</h1>
<button on:click={checkStatus}>Ping Database</button>
<p>Status: {status}</p>
<p>Message: {message}</p>
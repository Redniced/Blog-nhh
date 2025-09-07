import { writable } from 'svelte/store';

export const posts = writable([
  { id: 1, title: 'Welcome to My Blog', content: 'This is your first post!' },
  // Add more posts here
]);

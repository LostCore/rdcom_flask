#@date: 2017-8-25
#@title: How easily order WordPress post terms by hierarchy (with WBF)
Wordpress terms can be ordered hierarchical, but there is no built-in easy way to output them in this hierarchical order.
Say, for example, that you have this structure:

<pre>- Films
-- Comedy
---- '70
---- '90
---- modern
-- Historical
-- Science Fiction
</pre>

And you want to display a post categories like so: `Posted in: Films, Comedy, modern`

Functions like `wp_get_post_terms()` or `get_the_term_list()` doesn't help us.

At WAGA we had to do this task many times, so we include a pratical function in our **WBF Framework**.

**WBF** is as framework with the aim to make the WordPress development quickier and more enjoynable.

So, first we need to download and install WBF as plugin: you can grab it [here](http://update.waboot.org/resource/get/plugin/wbf).
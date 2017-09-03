#@date: 2017-8-25
#@title: How easily order WordPress post terms by hierarchy (with WBF)
Wordpress terms can be ordered hierarchical, but there is no built-in easy way to output them in this hierarchical order.
<br />Say, for example, that you have this structure:

<pre>
-- Films
-- Comedy
-- -- '70
-- -- '90
-- -- modern
-- Historical
-- Science Fiction
</pre>

<p>
And you want to display a post categories like so: `Posted in: Films, Comedy, modern`.  
Functions like `wp_get_post_terms()` or `get_the_term_list()` doesn't help us.
</p>

<p>
At WAGA we had to do this task many times, so we include a pratical function in our **WBF Framework**.
</p>

<p>
**WBF** is as framework with the aim to make the WordPress development quickier and more enjoynable.
</p>

<p>
So, first we need to download and install WBF as plugin: you can grab it [here](http://update.waboot.org/resource/get/plugin/wbf).  

After the activation you can now use the full power of the framework.
</p>

Test

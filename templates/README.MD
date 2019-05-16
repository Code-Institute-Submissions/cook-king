<H1>Cook-King</H1>
<h2><a href="http://cooking-app-doug.herokuapp.com/add_recipe" target="_blank">Deployed Website Link</a></h2>
<br>
This is a simple web-site that allows the user to view recipes created by other users, sorted by upvotes descending and filter them by three diffrent filters, add their own recipes and edit them.
<h3>IMPORTANT: There is one glitch, the multi select jquery plugin chosen, that I use doesn't work or display on mobile, 
as such when using developer tools you need to refresh the page so that it realises you are on mobile. This will allow it to display a normal multi-select</h3>
<H2>UX</h2>

<ul> 
<li>User Story: I am presented with a page full of recipes</li> 
<li>User Story: I filter the recipes to remove the allergens I am allergic too</li> 
<li>User Story: I can filter recipes by user they were created by or cuisine</li> 
<li>User Story: I can open any recipe I want and see its ingredients, allergens, a description and the method on making it.</li> 
<li>User Story: I can create my own recipe</li> 
<li>User Story: I can edit or delete the recipes I made but no one else can</li> 
<li>User Story: I can vote on recipes I like</li> 
<li>User Story: I can go on a users page and see their recipes or go on my own user page and see my recipes</li> 
</ul>

<a href="https://www.figma.com/file/dfXxW1Q4bMgBqKVG6HSRXJnQ/Untitled?node-id=0%3A1" target="_blank">Original Figma Wireframe</a>

<h2> Features </h2>

<ul> 
<li>Recipe website integraded with a mongodb database</li> 
<li>Users can create and edit their own recipes</li> 
<li>Users can create an account</li> 
<li>Simple and effective design</li> 
</ul>

<h2>Technologies Used</h2>

<ul> <li>Html 5</li> 
<li>Css</li> 
<li>Bootstrap</li>
<li>Javascript</li>
<li>Material Icons</li>
<li>JQuery</li> 
<a href="https://harvesthq.github.io/chosen/" target="_blank"><li>Chosen multi-select plugin</li></a>
</ul></li> </ul>

<h2>Testing</h2> 
I tested this project manually using developer tools and various devices.
I checked every page on desktop, mobile and tablet modes to make sure they displayed correctly.
I created test recipes, voted on them and edited them, to make sure they kept their votes.
I voted on recipes in different accounts to make sure I could only vote once on each.
I deleted recipes.
I filtered by every filter and combination of filters, to check that they were working correctly and the count was correct.
<h6>IMPORTANT: There is one glitch, the multi select jquery plugin chosen, that I use doesn't work or display on mobile, 
as such when using developer tools you need to refresh the page so that it realises you are on mobile. This will allow it to display a normal multi-select</h6>

Errors: <br>The only error that remains is an "Uncaught TypeError: Cannot read property 'split' of undefined" that does not effect functionality at all, <br>this seems to be linked to the toggle strict button that I used instead of the standard implementation, as it ussually only happens if you toggle strict off after toggling it on, <br>I fixed this by using a more normal strict mode implementation, <br>but chose to just leave it as it was for deployment because I liked the toggle button functionality and aesthetic.

<h2>Deployment</h2> Site was created in the cloud9 IDE. Then it was published to Heroku. <a href="http://cooking-app-doug.herokuapp.com/add_recipe" target="_blank">Link to Heroku Deployment</a>

<h2>Credits</h2> 
Recipes I added were from <a href="https://www.bbcgoodfood.com/recipes" target="_blank">BBC Good Food</a> 
<br> 
I got help on various glitches from fellow slack users on the code institute slack, this was very helpful.
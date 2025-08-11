# Online-auction-website
This project is a full featured e-commerce auction platform built with the Django framework. It allows users to post auction listings, browse active auctions, place bids and comment on items. Key features include a robust bidding system, category-based browsing and a personalized user watchlist to track items of interest.

## Getting Started
```
# Clone the repository
git clone https://github.com/bsteja33/Online-auction-website.git

# Navigate to the project directory
cd Online-auction-website

# Run the development server
python manage.py runserver
```

## Tech Stack
Python

Django Web Framework

Bootstrap

SQLite3

## Project Specification

The implementation of the auction site fulfills the following requirements:

**Models**: The application has at least three models in addition to the User model: one for auction listings, one for bids, and one for comments.

**Create Listing**: Users can visit a page to create a new listing. They can specify a title, a text-based description, a starting bid, and optionally provide a URL for an image and a category (e.g., Fashion, Toys, Electronics, Home).

**Active Listings Page**: The default route of the web application displays all currently active auction listings. For each listing, the page shows the title, description, current price, and photo (if one exists).

**Listing Page**: Clicking on a listing takes users to a page specific to that item, where they can view all details, including the current price.

If signed in, a user can add or remove the item from their "Watchlist."

If signed in, a user can bid on the item. The bid must be at least as large as the starting bid and greater than any other existing bids. If the bid is invalid, the user is presented with an error.

If the signed-in user is the creator of the listing, they have the ability to “close” the auction. This makes the highest bidder the winner and sets the listing to inactive.

If a user has won a closed auction, the page will display a notification message.

Signed-in users can add comments to the listing page, and all comments are displayed publicly.

**Watchlist**: Signed-in users can visit a Watchlist page that displays all listings they have added. Clicking on any listing takes the user to that listing’s page.

**Categories**: Users can visit a page that displays a list of all listing categories. Clicking on a category name takes the user to a page displaying all active listings in that category.

**Django Admin Interface**: A site administrator can use the Django admin interface to view, add, edit, and delete any listings, comments, and bids made on the site.



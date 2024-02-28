import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { HeaderComponent } from './header/header.component';
import { HomePageComponent } from './home-page/home-page.component';
import { FormsModule } from '@angular/forms';
import { TagsComponent } from "./tags/tags.component";
import { RouterModule } from '@angular/router';



@Component({
    selector: 'app-root',
    standalone: true,
    templateUrl: './app.component.html',
    styleUrl: './app.component.css',
    imports: [HeaderComponent, HomePageComponent, RouterOutlet, FormsModule, TagsComponent,RouterModule]
})
export class AppComponent {
  title = 'my-app';
}

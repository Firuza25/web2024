import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomePageComponent } from './home-page/home-page.component';
import { TagsComponent } from './tags/tags.component';

const routes: Routes = [
  {path:'', component:HomePageComponent},
  {path:'search/:searchTerm', component:HomePageComponent},
  {path:'tag/:tag', component:TagsComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }


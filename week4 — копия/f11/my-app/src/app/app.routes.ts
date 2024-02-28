import { Routes, RouterModule } from '@angular/router';
import { NgModule } from '@angular/core';
import { HomePageComponent } from './home-page/home-page.component';




export const routes: Routes = [
    {path:'', component: HomePageComponent},
    {path:'search/:searchTerm', component:HomePageComponent},//типа путь
    {path:'tag/:tag', component:HomePageComponent}
];


@NgModule({
    imports: [RouterModule],
    exports: [RouterModule]
  })

export class AppRoutingModule{}
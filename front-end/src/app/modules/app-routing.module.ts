import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {HomeComponent} from '../components/home/home.component';
import {PageNotFoundComponent} from '../components/page-not-found/page-not-found.component';
import {PathResolveService} from '../services/path-resolve/path-resolve.service';
import {paths} from '../configuration/app-paths';
import {AboutComponent} from '../components/about/about.component';
import {ContactComponent} from '../components/contact/contact.component';


const routes: Routes = [
  {
    path: '',
    redirectTo: paths.home,
    pathMatch: 'full'
  },
  {
    path: paths.home,
    component: HomeComponent,
  },
  {
    path: paths.about,
    component: AboutComponent,
  },
  {
    path: paths.contact,
    component: ContactComponent,
  },
  {
    path: '**',
    resolve: {
      path: PathResolveService
    },
    component: PageNotFoundComponent,
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}
